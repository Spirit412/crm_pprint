<template>
    <table class="striped">
        <thead>
        <tr>
            <!--            <th>#</th>-->
            <th>Номер штампа</th>
            <th>Z</th>
            <th>Высота штампа</th>
            <th>Эт по гор-ли</th>
            <th>Эт по верт-ли</th>
            <th>Отступ по гор-ли</th>
            <th>Отступ по верт-ли</th>
            <th>Файл cf2</th>
            <th>Файл mfg</th>
        </tr>
        </thead>

        <tbody>
        <tr v-for="(diecut, index) in diecuts" :key="diecut.cut_name">
            <td>{{ diecut.cut_name }}</td>
            <td>{{ diecut.zub_num }}</td>
            <td>{{ diecut.vsheet }}</td>
            <td>{{ diecut.hcountitem }}</td>
            <td>{{ diecut.vcountitem }}</td>
            <td>{{ diecut.hgap }}</td>
            <td>{{ diecut.vgap }}</td>
            <td>{{ diecut.cf2 }}</td>
            <td>{{ diecut.mfg }}</td>
            <!-- Кнопка в каждой строке  -->
            <td>
                <button class="btn-small btn" v-if=" userRole === 'admin' ">
                    <i class="material-icons">EDIT</i>
                </button>
                <button class="btn-small btn  disabled" v-else>
                    <i>EDIT</i>
                </button>
            </td>
        </tr>
        </tbody>
    </table>
</template>

<script>
    import {mapState, mapActions} from 'vuex'

    export default {
        name: "v-diecutstablecrud",
        data: () => ({
            userRole: null,
        }),
        computed: {
            ...mapState('diecut', ['diecuts']),

        },
        methods: {
            ...mapActions('diecut', ['GET_ALL_DIECUTS_FROM_API']),
            loadDiecuts () {
                this.GET_ALL_DIECUTS_FROM_API()
            }
        },
        mounted() {
            this.loadDiecuts()
            this.userRole = localStorage.getItem('role')
        }
    }

</script>

<style scoped>

</style>