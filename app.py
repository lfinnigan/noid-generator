from datetime import datetime
import streamlit as st

st.title("Temple Libraries bulk NOID generator")

st.markdown(
    """ 
    :rainbow[Fill out the form and get your NOIDS]
    """
)

collection_prefix = st.text_input(
    "Collection prefix. Must not contain invalid characters ('_' , '-', 'Q', 'X', 'Y', 'Z')", placeholder="Enter a valid collection prefix", max_chars=8)
noidcount = st.number_input("Number of NOIDs to generate",
                            step=1, format="%d", value=None, min_value=1, max_value=5000, placeholder="Enter a number from 1-5000")
startcount = st.number_input("Start count from (do not include zero padding)",
                             step=1, format="%d", value=1, min_value=1, max_value=999999)

if st.button("Generate NOIDs"):

    forbidden = set('_-QXYZ')

    if any(char in forbidden for char in collection_prefix):
        st.error(
            "Collection prefix contains invalid characters ('_' , '-', 'Q', 'X', 'Y', 'Z')")
    else:

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

        st.text_area(label="Copy and paste or download .tsv below",
                     value=output_data)

        st.download_button(
            label="Download NOIDs",
            data=output_data,
            file_name=f"noid_output{noiddate}.tsv",
            mime="text/tab-separated-values"
        )
