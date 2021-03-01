<template>
    <div>
        <div class="page-title">
            <h3>Таблица параметров Z</h3>
            <h5>Всего: {{ zubs_count }}</h5>
        </div>

        <vZubsTable
        />

        <section>

        </section>
    </div>
</template>

<script>
    import vZubsTable from "@/components/ZubsTable/v-zubstable";
    import {mapState} from 'vuex'

    export default {
        name: 'Zubs',
        data: () => ({
            loading: true,
        }),
        computed: {
            ...mapState('zub', ['zubs_count']),
        },
        components: {
            vZubsTable
        },
    }
</script>
