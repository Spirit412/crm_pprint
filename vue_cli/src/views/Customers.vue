<template>
    <div>
        <div class="page-title">
            <h3>Таблица заказчиков</h3>
        </div>
        <section>
            <vTableCustomer
                :customers_data="customers"
                :user-role="userRole"
            />
        </section>
    </div>

</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import vTableCustomer from "@/components/Customers/v-customer-table";
    import _ from 'lodash'

    export default {
        name: 'Customers',
        data() {
            return {
                loading: true,
                userRole: 'user',
                editing: false,
            }
        },
        components: {
            vTableCustomer
        },
        computed: {
            ...mapState('customer', ['customers']),

        },
        methods: {
            ...mapActions('customer', ['GET_ALL_CUSTOMERS_FROM_API']),
            loadCustomers() {
                this.GET_ALL_CUSTOMERS_FROM_API()
            }
        },
        mounted() {
            this.loadCustomers()
            this.userRole = localStorage.getItem('role')
        }
    }
</script>