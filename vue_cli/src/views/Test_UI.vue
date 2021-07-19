<template>
    <div id="test_ui" class="input-field col s6">

    
        <Autocomplete :items="zubs"
                      filterby="zub_num"
                      @change="onChange"
                      title="Список Z"
                      @selected="zubSelected"/>
        
        

    </div>
    
</template>

<script>
    import {mapState, mapActions} from 'vuex'

    import Autocomplete from '@/components/Autocomplete'
    export default {
        name: 'App',
        mounted() {
            this.loadZubs()
            this.zubs_to_input = this.zubs

        },
        data() {
            return {
                zubs_to_input: [],

            };
        },
        methods: {
            zubSelected(customer) {
                console.log(`Customer Selected:\nid: ${customer.id}\nname: ${customer.name}`);
            },
            onChange(value) {
                // do something with the current value
            },
            ...mapActions(
                'zub', ['GET_ALL_ZUBS_FROM_API']),
            loadZubs() {
                this.GET_ALL_ZUBS_FROM_API()
            },
        },
        components: {
            Autocomplete
        },
        computed: {
            ...mapState('zub', ['zubs']),
        },
    }
</script>

<style>

</style>