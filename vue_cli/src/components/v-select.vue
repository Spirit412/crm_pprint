<template>
    <div class="v-select">
        <p class="title"
           @click="areOptionsVisible = !areOptionsVisible"
        >{{selected}}</p>
        <div class="items"
             v-if="areOptionsVisible" >
            <p
                v-for="item in dataInput"
                :key="item.cut_name"
                @click="selectOption(item.cut_name)"
            >
                {{item.cut_name}}
            </p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "v-select",
        props: {
            dataInput: {
                type: Array,
                default: () => {
                    return []
                },
            },
            selected: {
                type: String,
                default: ''
            }
        },
        data() {
            return {
                areOptionsVisible: false
            }

        },
        methods: {
            selectOption(item) {
                this.$emit('select', item)
                this.areOptionsVisible = false
                console.log(item)
            },
            hideSelect() {
                this.areOptionsVisible = false
            }
        },
        mounted() {
            document.addEventListener('click', this.hideSelect.bind(this), true)
        },
        beforeDestroy() {
            document.removeEventListener('click', this.hideSelect)
        }
    }
</script>

<style>
    .v-select {
        position: relative;
        width: 200px;
        cursor: pointer;
    }

    .title {
        border: solid 1px #aeaeae;
    }

    .v-select p {
        margin: 0;
    }

    .items {
        border: solid 1px #aeaeae;
        position: absolute;
        top: 30px;
        z-index: 9999;
        background: white;
        right: 0;
        width: 100%;
    }

    .items p:hover {
        background: #aeaeae;
    }

</style>