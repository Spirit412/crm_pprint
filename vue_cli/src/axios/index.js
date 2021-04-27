import axios from 'axios'
import api_base_url from '@/my-conf'

axios.defaults.baseURL = 'http://localhost:8080/' 
// при работе с Docker 'http://app_FastAPI:8000/' 

axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token')
// axios.defaults.headers.common['Accept'] = 'application/json'
