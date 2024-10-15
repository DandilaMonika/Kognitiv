import mysql.connector
import streamlit as st

# Establish a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="kognitiv"
)

mycursor = mydb.cursor()  # Call the cursor method correctly
print("Connection Established")

# Create Streamlit app
def main():
    st.title("Kognitiv")

    # Display options in the sidebar
    option = st.sidebar.selectbox("Select an Option", ("Create", "View", "Update", "Delete"))

    # Perform Actions
    if option == "Create":
        st.subheader("Add Kognitiv Member")
        id = st.text_input("Enter your ID:")
        name = st.text_input("Enter your Name:")
        position = st.text_input("Enter your Position:")

        if st.button("Create"):
            sql = "INSERT INTO members (id, name, position) VALUES (%s, %s, %s)"
            val = (id, name, position)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record inserted successfully!")

    elif option == "View":
        st.subheader("View All Members")
        mycursor.execute("SELECT * FROM members")
        records = mycursor.fetchall()
    
    # Prepare data for the table
        if records:
            table_data = [{"ID": row[0], "Name": row[1], "Position": row[2]} for row in records]
            st.table(table_data)  # Display data as a table
        else:
            st.write("No records found.")


    elif option == "Update":
        st.subheader("Update Kognitiv Member")
        id = st.text_input("Enter the ID of the member you want to update:")
        new_name = st.text_input("Enter the new Name:")
        new_position = st.text_input("Enter the new Position:")

        if st.button("Update"):
            sql = "UPDATE members SET name = %s, position = %s WHERE id = %s"
            val = (new_name, new_position, id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record updated successfully!")

    elif option == "Delete":
        st.subheader("Delete Kognitiv Member")
        id = st.text_input("Enter the ID of the member you want to delete:")

        if st.button("Delete"):
            sql = "DELETE FROM members WHERE id = %s"
            val = (id,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record deleted successfully!")


if __name__ == "__main__":
    main()
