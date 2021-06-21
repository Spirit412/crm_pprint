<template>
    <div>
        <div class="page-title">
            <h3>Добавление штампа в БД</h3>
        </div>
        <section>
            <div class="row">
                <form class="col s6" @submit.prevent="submitForm">
                    <div class="row">
                        <div class="input-field col s6 form-group">
                            <input id="cut_name" type="text" v-model="form.cut_name" class="form-control"
                                   placeholder="номер штампа">
                            <label for="cut_name">Номер штампа</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="zub_num" type="text" v-model="form.zub_num" class="form-control"
                                   placeholder="номер зуба">
                            <label for="zub_num">Номер зуба</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="vsheet" type="text" v-model="form.vsheet" class="form-control"
                                   placeholder="высота штампа">
                            <label for="vsheet">Высота штампа</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="hcountitem" type="text" v-model="form.hcountitem" class="form-control"
                                   placeholder="количество этикеток вдоль направления печати">
                            <label for="hcountitem">Количество этикеток вдоль направления печати</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="vcountitem" type="text" v-model="form.vcountitem" class="form-control"
                                   placeholder="количество этикеток поперек направления печати">
                            <label for="vcountitem">Количество этикеток поперек направления печати</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="hgap" type="text" v-model="form.hgap" class="form-control"
                                   placeholder="расстояние между этикетками вдоль направления печати">
                            <label for="hgap">Расстояние между этикетками вдоль направления печати</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="vgap" type="text" v-model="form.vgap" class="form-control"
                                   placeholder="расстояние между этикетками поперек направления печати">
                            <label for="vgap">Расстояние между этикетками поперек направления печати</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="cf2" type="text" v-model="form.cf2" class="form-control"
                                   placeholder="имя файла cf2">
                            <label for="cf2">Имя файла cf2</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="mfg" type="text" v-model="form.mfg" class="form-control"
                                   placeholder="имя файла mfg">
                            <label for="mfg">Имя файла mfg</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <input id="pict" type="text" v-model="form.pict" class="form-control"
                                   placeholder="имя файла файла привью штампа">
                            <label for="pict">Имя файла файла привью штампа</label>
                        </div>
                        <div class="input-field col s6 form-group">
                            <textarea id="descript" v-model="form.descript" class="form-control"
                            ></textarea>
                            <label for="descript">Описание штампа</label>
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
        name: 'DiecutsAdd',
        data() {
            return {
                form:
                    {
                        cut_name: '',
                        zub_num: '',
                        vsheet: '',
                        hcountitem: '',
                        vcountitem: '',
                        hgap: '',
                        vgap: '',
                        cf2: '',
                        mfg: '',
                        pict: '',
                        descript: ''
                    }
            }
        },
        methods: {
            ...mapActions({
                adddiecut: "diecut/ADD_DIECUT"
            }),
            submitForm() {
                this.adddiecut(this.form)
            }
        },
        mounted() {
            this.userRole = localStorage.getItem('role')
            M.updateTextFields()
        }
    }
</script>