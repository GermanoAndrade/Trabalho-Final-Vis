mkdir -p ~/.streamlit/
echo "\
[theme]
base='dark'\n\
primaryColor = '#0595d5'\n\
font = 'sans serif'\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml