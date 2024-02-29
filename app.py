import streamlit as st
import pandas as pd
import hashlib

# Function to load or create services DataFrame
@st.cache(allow_output_mutation=True)
def load_services():
    try:
        services = pd.read_csv('services.csv')
    except FileNotFoundError:
        services = pd.DataFrame(columns=['Service', 'Priority', 'Type of Service', 'Description'])
    return services


# Function to save services DataFrame
def save_services(services):
    services.to_csv('services.csv', mode='a', header=False, index=False)


# Function to add a new service
def add_service(services, service, priority, type_of_service, description):
    new_service = pd.DataFrame({'Service': [service], 'Priority': [priority],
                                'Type of Service': [type_of_service], 'Description': [description]})
    services = pd.concat([services, new_service], ignore_index=True)
    return services

# Function to load or create users DataFrame
@st.cache(allow_output_mutation=True)
def load_users():
    try:
        users = pd.read_excel('login.xlsx')
    except FileNotFoundError:
        users = pd.DataFrame({'Username': [], 'Password': []})
    return users

# Function to save users DataFrame
def save_users(users):
    users.to_excel('login.xlsx', index=False)

import hashlib

# Function to authenticate user
def authenticate(username, password):
    users_df = load_users()

    # Check if username exists
    if not users_df['Username'].isin([username]).any():
        print("Username does not exist:", username)
        return False

    # Get hashed password from DataFrame
    hashed_password_df = users_df.loc[users_df['Username'] == username, 'Password'].iloc[0]

    # Hash input password
    hashed_password_input = hashlib.sha256(password.encode()).hexdigest()

    print("Username:", username)
    print("Hashed password from DataFrame:", hashed_password_df)
    print("Hashed input password:", hashed_password_input)

    # Compare hashed passwords
    if hashed_password_df == hashed_password_input:
        return True
    return False

# Function to sign up user
def signup(username, password):
    users_df = load_users()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Encode the password before hashing
    new_user = pd.DataFrame({'Username': [username], 'Password': [hashed_password]})
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    save_users(users_df)

# Main function
def main():
    st.title('Service Management System')

    # Authentication
    session_state = st.session_state
    if 'logged_in' not in session_state:
        session_state.logged_in = False

    # Load all services
    services = load_services()

    if not session_state.logged_in:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                session_state.logged_in = True
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")

        st.subheader("Sign Up if you are new")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            signup(new_username, new_password)
            st.success("Signup successful, you can now login.")

    else:
        st.header('Add New Service')

        new_service = st.text_input('Service')
        priority = st.selectbox('Priority', ['Low', 'Medium', 'High'])
        type_of_service = st.selectbox('Type of Service', ['Maintenance', 'Repair', 'Installation', 'Other'])
        description = st.text_area('Description')

        if st.button('Add Service'):
            services = add_service(services, new_service, priority, type_of_service, description)
            save_services(services)
            st.success(f"Service '{new_service}' added successfully!")

        st.header('Current Services')
        if services.empty:
            st.write('No services added yet.')
        else:
            st.write(services)

        st.write('© 2024 Service Management System')

if __name__ == '__main__':
    main()
