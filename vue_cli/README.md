# vue_cli

## Библиотека валидации Vuelidate
```
npm i vuelidate --save
```

## Библиотека стилей materialize
```
npm install materialize-css@next --save
```

## Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Настройка базового URL к API 
`src\axios\index.js`  
```
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
```

### Автоподстановка в headers поля 'Authorization' 
```
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token')
```

Все роуты  
```
src\router\index.js
```

Файл webpack.config.js - что бы WebStorm понимал ссылки типа `@/`