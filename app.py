import streamlit as st

# Set the title of the app
st.title("LegalEase")

# Add a heading for the "Generation" block
if st.button("Generation"):
    # Redirect to a new streamlit page for generation
    if st.button("Upload new template"):
        # Call a function to handle uploading new template
        upload_new_template()
    elif st.button("Work with existing template"):
        # Call a function to handle working with existing template
        work_with_existing_template()


# Add a heading for the "Understanding" block
if st.button("Understanding"):
    # Add content for the "Understanding" block
    st.write("This block is about understanding.")

# Run the app
if __name__ == "__main__":
    pass