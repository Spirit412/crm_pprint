<template>
    <div>
        <div class="page-title">
            <h3>Таблица цифровых заказов</h3>
        </div>
        <section>
            <vTable
                :data="data_djobs"
                :user-role="userRole"
            />
        </section>
    </div>

</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import vTable from "@/components/DJobsTable/v-djobs-table";
    import _ from 'lodash'

    export default {
        name: 'Djobs',
        data() {
            return {
                loading: true,
                userRole: 'user',
                editing: false,
            }
        },
        components: {
            vTable
        },
        computed: {
            ...mapState('djob', ['data_djobs']),

        },
        methods: {
            ...mapActions('djob', ['GET_ALL_DJOBS_FROM_API']),
            loadDjobs() {
                this.GET_ALL_DJOBS_FROM_API()
            }
        },
        mounted() {
            this.loadDjobs()
            this.userRole = localStorage.getItem('role')
        }
    }
</script>