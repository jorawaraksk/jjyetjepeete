import speedtest

def run_speedtest():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    return f"Download: {st.results.download / 1e6:.2f} Mbps\nUpload: {st.results.upload / 1e6:.2f} Mbps"
