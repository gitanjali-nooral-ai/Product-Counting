import streamlit as st
import requests
import pandas as pd


API_URL = "http://127.0.0.1:8000"



st.set_page_config(

    page_title="Product Counting System",

    layout="wide"

)



st.title(
    "📦 Customer Product Detection System"
)



# -------------------------
# Product Registration
# -------------------------


st.header(
    "Register Product"
)



product_name = st.text_input(

    "Product Name"

)



image = st.file_uploader(

    "Upload Product Image",

    type=[
        "jpg",
        "jpeg",
        "png"
    ]

)



if st.button(
    "Register Product"
):


    if product_name and image:


        response=requests.post(

            API_URL+"/products/upload",

            files={

                "image":

                (

                    image.name,

                    image.getvalue(),

                    image.type

                )

            },

            data={

                "name":

                product_name

            }

        )


        if response.status_code==200:


            st.success(

                response.json()

            )

        else:

            st.error(

                response.text

            )



# -------------------------
# Products
# -------------------------


st.divider()



st.header(

    "Available Products"

)



if st.button(

    "Refresh Products"

):


    result=requests.get(

        API_URL+"/products/"

    )



    products=result.json()["products"]



    st.session_state.products=products




products=st.session_state.get(

    "products",

    []

)



if products:


    selected=st.selectbox(

        "Select Product",

        products,

        format_func=lambda x:x[1]

    )


else:


    selected=None



# -------------------------
# Camera Control
# -------------------------


st.divider()


st.header(

    "Camera Control"

)



if selected:


    col1,col2=st.columns(2)



    with col1:


        if st.button(

            "Start Camera"

        ):


            result=requests.post(

                API_URL+

                f"/camera/start/{selected[0]}"

            )


            st.success(

                result.json()

            )




    with col2:


        if st.button(

            "Stop Camera"

        ):


            result=requests.post(

                API_URL+

                "/camera/stop"

            )


            st.info(

                result.json()

            )



# -------------------------
# Camera Status
# -------------------------


st.divider()


st.header(

    "System Status"

)



status=requests.get(

    API_URL+"/camera/status"

).json()



if status["running"]:


    st.success(

        "Camera Running"

    )

else:


    st.warning(

        "Camera Stopped"

    )



# -------------------------
# Count Reports
# -------------------------


st.divider()


st.header(

    "Production Reports"

)



if st.button(

    "Load Count Events"

):


    data=requests.get(

        API_URL+"/reports/counts"

    ).json()



    events=data["events"]



    df=pd.DataFrame(

        events,

        columns=[

            "Product",

            "Tracking ID",

            "Time"

        ]

    )


    st.dataframe(

        df,

        use_container_width=True

    )



if st.button(

    "Generate CSV"

):


    result=requests.get(

        API_URL+"/reports/csv"

    )


    path=result.json()["file"]


    with open(

        path,

        "rb"

    ) as file:


        st.download_button(

            label="Download CSV",

            data=file,

            file_name="count_report.csv"

        )