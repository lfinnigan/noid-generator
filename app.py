from datetime import datetime
import streamlit as st

st.title("Temple Libraries bulk NOID generator")

st.markdown(
    """ 
    :rainbow[Fill out the form and download your NOIDS]
    """
)

collection_prefix = st.text_input("Collection prefix")
noidcount = st.number_input("Number of NOIDs to generate", step=1, format="%d")
startcount = st.number_input("Start count from", step=1, format="%d", value=1)

if st.button("Generate NOIDs"):

    # Get date
    today = datetime.today()
    noiddate = today.strftime('%Y%m')

    # Get consecutive count beginning with startcount
    counts = range(startcount, startcount + noidcount)

    noid_list = []

    for c in counts:
        pcount = str(c).rjust(6, '0')
        noidid = collection_prefix + "Z" + noiddate + pcount
        noid_list.append(noidid)

    st.write(f"{int(noidcount)} NOIDs generated")

    output_data = "\n".join(noid_list)
    st.download_button(
        label="Download NOIDs",
        data=output_data,
        file_name=f"noid_output{noiddate}.tsv",
        mime="text/tab-separated-values"
    )

    st.text_area(label="Preview", value=output_data)
