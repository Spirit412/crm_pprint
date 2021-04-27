<template>
    <form class="card auth-card" @submit.prevent="submit">
        <div class="card-content">
            <span class="card-title">CRM Pprint 1.0</span>
            <div class="input-field">
                <input
                        id="email"
                        type="text"
                        v-model.trim="logform.email"
                        :class="{
            invalid:
              ($v.logform.email.$dirty && !$v.logform.email.required) ||
              ($v.logform.email.$dirty && !$v.logform.email.email),
          }"
                />
                <label for="email">Email</label>
                <small
                        class="helper-text invalid"
                        v-if="$v.logform.email.$dirty && !$v.logform.email.required"
                >Поле Email не должно быть пустым</small
                >
                <small
                        class="helper-text invalid"
                        v-else-if="$v.logform.email.$dirty && !$v.logform.email.email"
                >Введите корректный Email</small
                >
            </div>
            <div class="input-field">
                <input
                        id="password"
                        type="password"
                        v-model.trim="logform.password"
                        :class="{
            invalid:
              ($v.logform.password.$dirty && !$v.logform.password.required) ||
              ($v.logform.password.$dirty && !$v.logform.password.minLength),
          }"
                />
                <label for="password">Пароль</label>
                <small
                        class="helper-text invalid"
                        v-if="$v.logform.password.$dirty && !$v.logform.password.required"
                >Введите пароль</small
                >
                <small
                        class="helper-text invalid"
                        v-else-if="$v.logform.password.$dirty && !$v.logform.password.minLength"
                >Длина не менее {{ $v.logform.password.$params.minLength.min }} символов.
                    Сейчас он {{ logform.password.length }}</small
                >
            </div>

        </div>
        <div class="card-action">
            <div>
                <button class="btn waves-effect waves-light auth-submit" type="submit">
                    Войти
                    <i class="material-icons right">send</i>
                </button>
            </div>

        </div>
    </form>
</template>


<script>
    import {email, required, minLength} from "vuelidate/lib/validators";
    import {mapGetters, mapActions} from 'vuex'

    export default {
        name: 'login',
        validations: {
            logform: {
                password: {required, minLength: minLength(4)},
                email: {required, email},
            }
        },
        data() {
            return {
                logform: {
                    email: null,
                    password: null,
                }
            }
        },

        methods: {
            ...mapActions({
                loginUser: 'user/LOGIN_USER'
            }),
            submit() {
                this.loginUser(this.logform)
                    .then(() => this.$router.push('/'))
                    .catch(err => console.log(err))
            },
            clear() {
                this.$v.$reset()
                this.email = ''
                this.password = ''
            },
        },
        computed: {
            passErrors() {
                const errors = []
                if (!this.$v.logform.password.$dirty) return errors
                !this.$v.logform.password.minLength && errors.push('password must be at most 6 characters long')
                !this.$v.logform.password.required && errors.push('password is required.')
                return errors
            },
            emailErrors() {
                const errors = []
                if (!this.$v.logform.email.$dirty) return errors
                !this.$v.logform.email.email && errors.push('Must be valid e-mail')
                !this.$v.logform.email.required && errors.push('E-mail is required')
                return errors
            },
        },
    }
</script>
