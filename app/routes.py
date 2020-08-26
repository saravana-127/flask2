import json
import uuid
import pandas as pd
from flask import Flask,jsonify,request,render_template
from sqlalchemy.sql import label
from sqlalchemy import func,distinct
from app import db,app
from app.models import User

@app.route('/getusers',methods=['GET'])
def getuserslist():
    try:
        all_user=User.query.all()
        if not all_user:
            return jsonify({'message':"No Active user was found"}) 
        userlist=[]
        for user in all_user:
            data={}
            data['id']=user.id
            data['username']=user.username
            data['department']=user.department
            userlist.append(data)
        return jsonify({'message':userlist}),200  
    except:
        return jsonify({'message':"No user found"}),400      

@app.route('/createuser',methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        newuser = User(username=data['username'],department=data['department'])
        db.session.add(newuser)
        db.session.commit()
        return jsonify({'message':'newuser sucessfully created'}),201
    except:
        return jsonify({'message':"Please provide the valid data"}),400        

@app.route('/updateuser/<id>',methods=['PUT'])
def update_user(id):
    try: 
        data = request.get_json()
        user=User.query.filter_by(id = id).first()
        user.username = data['username']
        user.department=data['department']
        db.session.commit()
        return jsonify({'message':data}),200
    except:
        return jsonify({'message':"No user found"}),404        

@app.route('/deleteuser/<id>',methods=['DELETE'])
def delete_user(id):
    try:
        user=User.query.filter_by(id = id).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message':'deleted Successfully'}),200 
    except:
        return jsonify({'message':'not a valid user'}),404   


@app.route('/searchuser/<username>',methods=['GET'])
def search_user_by_name(username):
    try:
        user=username.lower()
        username = User.query.filter_by(username=user).first()
        data={}
        data['id']=username.id
        data['username']=username.username
        data['department']=username.department
        return jsonify({'message':data}),200
    except:
        return jsonify({'message':'not a valid user'}),404   

@app.route('/searchdept/<department>',methods=['GET'])
def search_user_by_department(department):
    try:
        dept=department.lower()
        username = User.query.filter_by(department=dept).all()
        dept_list=[]
        for user in username:
            data={}
            data['id']=user.id
            data['username']=user.username
            data['department']=user.department
            dept_list.append(data)
        return jsonify({'message':dept_list}),200 
    except:    
        return jsonify({'message':'not a valid department'}),400   


@app.route('/barchart',methods=['GET'])
def student_barchart():
    student_datas= db.session.query(label('department',User.department),label('count',func.count(User.department))).group_by(User.department).all()
    student_list=[]
    for user in student_datas:
            student_data={}
            student_data['department']=user.department
            student_data['count']=user.count
            student_list.append(student_data)
    output=json.dumps(student_list)
    df=pd.read_json(output)
    df.to_csv('new.csv',index=False)
    return render_template('chart.html',values=student_list)

#@app.route('/csv',methods=['GET'])
#def csvfile():
#    url='/home/bahulashree/flasktask/new.csv'
#    with open(url,'r') as f:
#        content=f.read()
#        return content
