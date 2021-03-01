import axios from 'axios'


axios.defaults.baseURL = 'http://10.5.0.6:8000/' 
// при работе с Docker 'http://app_FastAPI:8000/' 

// axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token')
// axios.defaults.headers.common['Accept'] = 'application/json'
