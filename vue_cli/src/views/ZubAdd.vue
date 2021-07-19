<template>
    <div>
        <div class="page-title">
            <h3>Добавление Z в БД</h3>
        </div>
        <section>
            <div class="row">
                <form class="col s6" @submit.prevent="submitForm">
                    <div class="row">
                        <div class="input-field col s6 form-group">
                            <input id="zub_num" type="text" v-model="form.zub_num" class="form-control"
                                   placeholder="номер зуба">
                            <label for="zub_num">Номер зуба</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="hprint" type="text" v-model="form.hprint" class="form-control"
                                   placeholder="высота штампа">
                            <label for="hprint">Высота штампа</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="hpolimer" type="text" v-model="form.hpolimer" class="form-control"
                                   placeholder="длина полимера 1.14">
                            <label for="hpolimer">Длина полимера 1.14</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="hpolimer_17" type="text" v-model="form.hpolimer_17" class="form-control"
                                   placeholder="длина полимера 1.7">
                            <label for="hpolimer_17">Длина полимера 1.7</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <button class="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>
        </section>
    </div>

</template>

<script>
    import {mapState, mapActions} from 'vuex'

    export default {
        name: 'ZubAdd',
        data() {
            return {
                form:
                    {
                        zub_num: '',
                        hprint: '',
                        hpolimer: '',
                        hpolimer_17: '',
                    }
            }
        },
        methods: {
            ...mapActions({
                addzub: "zub/ADD_ZUB"
            }),
            submitForm() {
                this.addzub(this.form)
            }
        },
        mounted() {
            this.userRole = localStorage.getItem('role')
            M.updateTextFields()
        }
    }
</script>