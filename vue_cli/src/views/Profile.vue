<template>
  <div>
    <div class="page-title">
      <h3>Профиль</h3>
    </div>
      <div>
          <h5>Имя: {{name}}</h5>
          <h5>email: {{email}}</h5>
          <h5>Роль: {{role}}</h5>
          <span class="helper-text invalid">роль ограничивает доступ к ресурсам системы</span>
          <h5>Описание: {{description}}</h5>
      </div>

<!--    <form class="form">-->
<!--      <div class="input-field">-->
<!--        <input id="description" type="text" />-->
<!--        <label for="description">Имя</label>-->
<!--        <span class="helper-text invalid">name</span>-->
<!--      </div>-->

<!--      <button class="btn waves-effect waves-light" type="submit">-->
<!--        Обновить-->
<!--        <i class="material-icons right">send</i>-->
<!--      </button>-->
<!--    </form>-->
  </div>
</template>


<script>
    import {mapGetters, mapActions} from 'vuex'

    export default {
        data: () => ({
            email: null,
            name: null,
            description: null,
            role: null
        }),

        mounted() {
            // // // Если токен или имя пустые, перенаправлять на страницу логина.
            if (localStorage.getItem('token') && localStorage.getItem('name')) {
                this.name = localStorage.getItem('name')
                this.email = localStorage.getItem('email')
                this.description = localStorage.getItem('description')
                this.role = localStorage.getItem('role')
                console.log('Проверка. Из локального хранилища: localStorage.getItem(\'name\'): ' + localStorage.getItem('name'))
            } else {
                this.$router.push('/login')
            }
        }
    }
</script>