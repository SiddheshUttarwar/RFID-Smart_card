import os
import datetime
from prettytable import PrettyTable
from time import sleep
from database import student_data
from RFID import get_card
from sms import Sendsms
from attendance import get_attendance
from canteen import FoodMenu
from library import Library
from student_books import Student_Books
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tabulate import tabulate
import smtplib
import ssl
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

student = student_data()
food = FoodMenu()
library = Library()
books = Student_Books()


def get_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    return filename


def mail_details(card):
    details = student.get_Details(card)
    name = details['name']
    rollno = details['rollno']
    email = 'uttarwarsiddhesh@gmail.com'
    phone = details['Phone']
    resume = details['resume']
    message = MIMEMultipart()
    message["Subject"] = "Student Details - "+name
    body = f"""
        \n Name = {name}
        \n Roll No = {rollno}
        \n Phone Number = {phone}
        \n Email Id = {email}
    """
    message.attach(MIMEText(body, "plain"))
    resume = student.get_documents(card)
    with open(resume, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {resume}",
        )
        message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    password = 'ybkmdgsvztzlrgee'
    receivers = input("Enter the receivers mail id").split(',')
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email, password)
            for i in receivers:
                server.sendmail(email, i, text)
        print('email sent')
    except:
        print("wrong EmailID or Password ")
        print("Email Not sent")


def get_student_details(card):
    details = student.get_Details(card)
    name = details['name']
    rollno = details['rollno']
    email = details['email']
    phone = details['Phone']
    resume = details['resume']
    body = f"""
        \n Name = {name}
        \n Roll No = {rollno}
        \n Phone Number = {phone}
        \n Email Id = {email}
    """
    print(body)


def update_details(card):
    print("Enter")
    print("1.Update Name")
    print("2.Update Rollno")
    print("3.Upade Email Id")
    print("4.Update Phone number")
    print("5.Upade resume")
    print("6.To update complete details")

    op = input("Enter the number for required operation")

    if op == "1":
        name = input("Enter the New Name :")
        student.update_name(card, name)
    if op == "2":
        Roll = input("Enter the new roll no : ")
        student.update_rollno(card, Roll)
    if op == "3":
        email = input("Enter the new email id :")
        student.update_email(card, email)
    if op == '4':
        phone = input("enter the New Phone number")
        student.update_phone(card, phone)
    if op == '5':
        resume = get_file()
        student.update_resume(card, resume)
    if op == '6':
        name = input("Enter the New Name :")
        student.update_name(card, name)
        Roll = input("Enter the new roll no : ")
        student.update_rollno(card, Roll)
        email = input("Enter the new email id :")
        student.update_email(card, email)
        phone = input("enter the New Phone number")
        student.update_phone(card, phone)
        Resume = input("enter the New Resume")
        student.update_resume(card, Resume)


def add_student_details(card):
    print("<----- Enter Details to Register ----->")
    name = input("Enter the name : ")
    rollno = input("Enter the Roll no : ")
    email = input("Enter the institute email : ")
    phone = input("Enter Phone Number : ")
    print()
    print("The resume should be in pdf format only...")
    resume = get_file()
    student.insert_data(card, rollno, name, email, phone, resume)


def send_payment_link(card):
    canteen = food.get_table()
    print()
    create_tabel(canteen)
    data = student.get_phone(card)
    phone = "+91"+data
    print()
    userinput = list(map(int, input("Enter the ids of the food you want to order : ").split()))
    amount = get_price(userinput)
    message = f"You have been requested payment of Rs. {amount}"
    print()
    try:
        Sendsms(message, amount, phone)
    except:
        pass
    else:
        print("Device not registered with twilio")
    create_receit(userinput)
    print()


def books_table(data):
    table = []
    header = ['ID', 'Book']
    for i in data:
        x = [i["_id"], i['book_name']]
        table.append(x)
    print(tabulate(table, headers=header))


def create_tabel(data):
    table = []
    header = ['id', 'Item', 'Price']
    for i in data:
        x = [i["id"], i['dish'], i['price']]
        table.append(x)
    print(tabulate(table, headers=header))


def get_price(userinput):
    canteen = food.get_table()
    price = 0
    for i in userinput:
        for item in canteen:
            if item['id'] == i:
                price += item['price']
                break
    return price


def create_receit(userinput):
    pretty = PrettyTable(['item', 'price'])
    canteen = food.get_table()
    price = 0
    for i in userinput:
        for item in canteen:
            if item['id'] == i:
                price += item['price']
                pretty.add_row([item['dish'], item['price']])
                break
    print('<---- Receit ---->')
    print(pretty)
    print(f'---- total : {price} ----')


def borrow_books(card):
    id = student.get_rollno(card)
    print()
    data = library.get_library()
    books_table(data)
    books_ids = input("Enter the book ids you want to borrow : ")
    books.add_data(id, books_ids)
    print()
    date = datetime.datetime.now() + datetime.timedelta(days=15)
    print("Your Book return date is :", date)


if __name__ == "__main__":
    print("----------Welcome to Smart student Interface----------")

    print("Scan your ID card")
    card = (input())

    while True:

        print("Select")
        print("1.Take attendance")
        print("2.Extract attendance")
        print("3.Get Student details")
        print("4.Order food")
        print("5.Mail Student details")
        print("6.Update Student details")
        print("7.Add Student details")
        print("8.Borrow Books from Library")
        print("9.Exit")
        print()
        option = input("Enter the number for required option : ")

        if option == "1":
            print("The attendance is getting collected")
            print()
            print("scan your card to give your attendance")
            x = get_attendance()
            with open("attendance.txt", 'w') as files:
                for i in x:
                    files.write(str(i)+'   ')
        if option == '2':
            with open("attendance.txt", 'r') as files:
                for i in files:
                    print(i)
        if option == '3':
            get_student_details(card)
            print()
        if option == '4':
            send_payment_link(card)
            print()
        if option == '5':
            mail_details(card)
            print()
        if option == '6':
            update_details(card)
            print()
        if option == '7':
            add_student_details(card)
            print()
        if option == '8':
            borrow_books(card)
            print()
        if option == '9':
            break

        sleep(10)
