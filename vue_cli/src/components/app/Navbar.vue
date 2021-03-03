<template>

    <nav class="navbar orange lighten-1">
        <div class="nav-wrapper">
            <div class="navbar-left">
                <a href="#" @click.prevent="$emit('click-hide-navbar')">
                    <i class="material-icons black-text">dehaze</i>
                </a>
                <span class="black-text">{{ date | date('datetime') }}</span>
            </div>

            <ul class="right hide-on-small-and-down">
                <li>
                    <a
                        class="dropdown-trigger black-text"
                        href="#"
                        data-target="dropdown"
                        ref="dropdown"
                    >
                        {{ name }}
                        <i class="material-icons right">arrow_drop_down</i>
                    </a>

                    <ul id="dropdown" class="dropdown-content">
                        <li>
                            <router-link to="/profile" class="black-text">
                                <i class="material-icons">account_circle</i>Профиль
                            </router-link>
                        </li>
                        <li class="divider" tabindex="-1"></li>
                        <li>
                            <a href="#" class="black-text" @click.prevent="logout">
                                <i class="material-icons">assignment_return</i>Выйти
                            </a>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
    import {mapGetters, mapActions} from 'vuex'

    export default {
        data: () => ({
            date: new Date(),
            interval: null,
            dropdown: null,
            email: null,
            name: null,
        }),

        methods: {
            logout: function () {
                // mapActions('user/LOGOUT')
                this.$store.dispatch('user/LOGOUT')
                this.$router.push('/login')
            }


        },

        mounted() {
            //Если токен или имя пустые, перенаправлять на страницу логина.
            // if (localStorage.getItem('token') && localStorage.getItem('name')) {
            //     this.name = localStorage.getItem('name')
            //     console.log('Проверка. Из локального хранилища: localStorage.getItem(\'name\'): ' + localStorage.getItem('name'))
            // } else {
            //     this.$router.push('/login')
            // }

            this.interval = setInterval(() => {
                this.date = new Date()
            }, 1000)
            // console.log(this.$refs);
            this.dropdown = M.Dropdown.init(this.$refs.dropdown, {
                constrainWidth: false
            })
        },
        computed: {
            theme() {
                return (this.$vuetify.theme.dark) ? 'dark' : 'light'
            }
        }
        // beforeDestroy() {
        //   console.log('before Destroy')
        //   clearInterval(this.interval)
        //   if (this.dropdown && this.dropdown.destroy) {
        //     this.dropdown.destroy()
        //   }
        // }
    }
</script>
