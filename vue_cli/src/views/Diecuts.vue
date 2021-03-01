<template>
    <div>
        <div class="page-title">
            <h3>Таблица штампов</h3>
            <h5>Всего штампов в таблице: {{ diecuts_count }}</h5>
            <!--            <h5>Всего штампов в таблице: XXX</h5>-->
        </div>
        <section>
            <vDieCutsTableCRUD
            />
        </section>
    </div>

</template>

<script>
    import vDieCutsTableCRUD from "@/components/DieCutsTable/v-diecutstablecrud";
    import {mapState} from 'vuex'

    export default {
        name: 'Diecuts',
        data: () => ({
            loading: true,
        }),
        computed: {
            ...mapState('diecut', ['diecuts_count']),
        },
        components: {
            vDieCutsTableCRUD
        },
    }
</script>

