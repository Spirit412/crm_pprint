<template>
    <div>
        <div class="page-title">
            <h3>Таблица штампов</h3>
            <h6>Штампов: {{ diecuts.length }}</h6>
        </div>
        <section>
            <vTable
                :diecuts_data="diecuts"
                :user-role="userRole"
            />
        </section>
    </div>

</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import vTable from "@/components/DieCutsTable/v-table";
    import _ from 'lodash'

    export default {
        name: 'Diecuts',
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
            ...mapState('diecut', ['diecuts']),
            
        },
        methods: {
            ...mapActions('diecut', ['GET_ALL_DIECUTS_FROM_API']),
            loadDiecuts() {
                this.GET_ALL_DIECUTS_FROM_API()
            }
        },
        mounted() {
            this.loadDiecuts()
            this.userRole = localStorage.getItem('role')
        }
    }
</script>