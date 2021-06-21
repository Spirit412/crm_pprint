<template>
  <form class="card auth-card" @submit.prevent="submitForm">
    <div class="card-content">
      <span class="card-title">Домашняя бухгалтерия</span>
      <div class="input-field">
        <input
          id="email"
          type="text"
          v-model.trim="regform.email"
          :class="{
            invalid:
              ($v.regform.email.$dirty && !$v.regform.email.required) ||
              ($v.regform.email.$dirty && !$v.regform.email.email),
          }"
        />
        <label for="email">Email</label>
        <small
          class="helper-text invalid"
          v-if="$v.regform.email.$dirty && !$v.regform.email.required"
          >Поле Email не должно быть пустым</small
        >
        <small
          class="helper-text invalid"
          v-else-if="$v.regform.email.$dirty && !$v.regform.email.email"
          >Введите корректный Email</small
        >
      </div>
      <div class="input-field">
        <input
          id="password"
          type="password"
          v-model.trim="regform.password"
          :class="{
            invalid:
              ($v.regform.password.$dirty && !$v.regform.password.required) ||
              ($v.regform.password.$dirty && !$v.regform.password.minLength),
          }"
        />
        <label for="password">Пароль</label>
        <small
          class="helper-text invalid"
          v-if="$v.regform.password.$dirty && !$v.regform.password.required"
          >Введите пароль</small
        >
        <small
          class="helper-text invalid"
          v-else-if="$v.regform.password.$dirty && !$v.regform.password.minLength"
          >Длина не менее {{ $v.regform.password.$params.minLength.min }} символов.
          Сейчас он {{ regform.password.length }}</small
        >
      </div>
<!--      Поле ИМЯ-->
      <div class="input-field">
        <input
          id="name"
          type="text"
          v-model.trim="regform.name"
          :class="{ invalid: $v.regform.name.$dirty && !$v.regform.name.required }"
        />

        <label for="name">Имя</label>
        <small
          class="helper-text invalid"
          v-if="$v.regform.name.$dirty && !$v.regform.name.required"
        >
          Введите ваше имя
        </small>
      </div>
      <p>
        <label>
          <input type="checkbox" v-model="regform.agree" />
          <span>С правилами согласен</span>
        </label>
      </p>
    </div>
    <div class="card-action">
      <div>
        <button class="btn waves-effect waves-light auth-submit" type="submit">
          Зарегистрироваться
          <i class="material-icons right">send</i>
        </button>
      </div>

      <p class="center">
        Уже есть аккаунт?
        <router-link to="/login">Войти!</router-link>
      </p>
    </div>
  </form>
</template>

<script>
import { email, required, minLength } from "vuelidate/lib/validators";
import {mapGetters, mapActions} from 'vuex'

export default {
  name: "register",
  data() {
    return {
      regform: {
        email: "",
        password: "",
        name: "",
        agree: false
      }
    }
  },
  validations: {
    regform: {
      email: {
        email,
        required
      },
      password: {
        required,
        minLength: minLength(3)
      },
      name: {
        required
      },
      agree: {
        checked: (v) => v
      }
    },
  },
  methods: {
    ...mapActions({
      regUser: 'user/REGISTER_USER'
    }),
      submitForm() {
      this.regUser({'email': this.regform.email, 'password': this.regform.password, 'name': this.regform.name})
        .then(() => this.$router.push('/'))
        .catch(err => console.log(err))

    },
  },
};
</script>
