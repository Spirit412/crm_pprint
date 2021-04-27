<template>
    <div>
        <div class="page-title">
            <h3>Создание цифрового заказа</h3>
        </div>
        <section>
            <div class="row">
                <form class="col s6" action="" method="post">
                    <div class="row">
                        <vSelect
                            :dataInput="diecuts"
                            @select="optionSelect"
                            :selected="selected"
                        />
                    </div>
                    <p>{{selected}}</p>
                    <div class="row">
                        <div class="input-field col s6">
                            <input id="job_number" type="text" class="validate">
                            <label for="job_number">Номер заказа</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s6">
                            <input id="costumer_name" type="text" class="validate">
                            <label for="costumer_name">Заказчик</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s6">
                            <input id="diecut" :placeholder="selected" type="text" class="validate" :value="selected">
                            <label for="diecut">Штамп {{selected}}</label>
                        </div>
                    </div>

                    <div class="row">
                        <div class="input-field col s6">
                            <input id="bleed" type="text" class="validate">
                            <label for="bleed">Bleed</label>
                        </div>
                    </div>
                </form>
            </div>
        </section>
    </div>

</template>

<script>
    import _ from 'lodash'
    import vSelect from '@/components/v-select'
    import {mapState, mapActions} from 'vuex'

    export default {
        name: 'DjobsAdd',
        components: {
            vSelect,
        },
        data() {
            return {
                diecut_cut_name: '',
                bleed: '',
                razmeshenie: '',
                digitaljob_num: '',
                customer_id: '',
                color_print: ['cmyk', 'b&w'],
                descript: '',
                frames: [
                    {
                        frame_num: '',
                        descript: '',
                        rows: [
                            {
                                descript: '',
                                design_url: '',
                                row_number: '',
                                design_angle_rotate: '',
                            }
                        ],

                    }
                ],

                loading: true,
                userRole: 'user',
                editing: false,
                selected: 'Cut',
            }
        },
        computed: {
            ...mapState('diecut', ['diecuts']),

        },
        methods: {
            ...mapActions('diecut', ['GET_ALL_DIECUTS_FROM_API']),
            loadDiecuts() {
                console.info('вызов mapActions GET_ALL_DIECUTS_FROM_API')
                this.GET_ALL_DIECUTS_FROM_API()
            },
            optionSelect(option) {
                this.selected = option
            },
        },
        mounted() {
            this.loadDiecuts()
            this.userRole = localStorage.getItem('role')
        }
    }
</script>