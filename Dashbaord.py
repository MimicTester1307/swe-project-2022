import streamlit as st
import pandas as pd
import sqlite3 
import hashlib # other alternatives include: passlib,hashlib,bcrypt,scrypt

#security function
def secure_pass(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_pass(password,hashed_text):
	if secure_pass(password) == hashed_text:
		return hashed_text
	return False


# DB Management
conn = sqlite3.connect('clients.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)')

def add_users(username,password):
	c.execute('INSERT INTO users(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM users WHERE username =? AND password = ?',(username,password))
	user = c.fetchall()
	return user


def view_all_users():
	c.execute('SELECT * FROM users')
	data = c.fetchall()
	return data



def main():
	"""NFT Project Dashboard"""

	st.title("NFT Project Dashboard")

	menu = ["Home","Login","SignUp"]
	option = st.sidebar.selectbox("Menu",menu)

	if option == "Home":
		st.subheader("Home")

	elif option == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			create_usertable()
			hashed_pswd = secure_pass(password)

			result = login_user(username,check_pass(password,hashed_pswd))
			if result:

				st.success("Welcome Back {}".format(username))

				task = st.selectbox("Task",["Measure the community of an NFT", "Track an NFT performance"," Check your profile"])
				if task == "Measure the community of an NFT":
					st.subheader("Measure the community of an NFT")






				elif task == "Track an NFT performance":
					st.subheader("Track an NFT performance")





				elif task == "Check your profile":
					st.subheader("Check your profile")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif option == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_users(new_user, secure_pass(new_password))
			st.success("Account successfully created")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
