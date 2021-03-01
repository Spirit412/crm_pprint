<template>
    <table class="striped">
        <thead>
        <tr>
            <!--            <th>#</th>-->
            <th>Z</th>
            <th>Длина печати</th>
            <th>Длина полимера 1.16</th>
            <th>Длина полимера 1.7</th>
            <!--                    <th>Открыть</th>-->
        </tr>
        </thead>

        <tbody>
        <tr v-for="(zub, index) in zubs" :key="zub.zub_num">
            <!-- индексация  массива-->
            <td>{{ zub.zub_num }}</td>
            <td>{{ zub.hprint }}</td>
            <td>{{ zub.hpolimer }}</td>
            <td>{{ zub.hpolimer_17 }}</td>

        </tr>
        </tbody>
    </table>
</template>

<script>
    import {mapState, mapActions} from 'vuex'

    export default {
        name: "v-zubstable",
        computed: {
            ...mapState('zub', ['zubs'])
        },
        methods: {
            ...mapActions('zub', ['GET_ALL_ZUBS_FROM_API']),
            loadZubs () {
                this.GET_ALL_ZUBS_FROM_API()
            }
        },
        mounted() {
            this.loadZubs()
        }
    }

</script>
