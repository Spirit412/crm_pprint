<template>
    <div class="v-table-row">
        <div class="row row__number bold">{{index+1}}</div>
        <div class="row row__name bold">{{row_data.name}}</div>
        <div class="row row__descript">{{row_data.descript}}</div>
        <div class="row row__tbl_edit" v-if="user_role === 'admin'">
            <button class="btn-small btn">
                <i class="material-icons">mode_edit</i>
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "v-table-row",
        props: {

            index: {
                type: Number,
                default: () => {
                    return {}
                }
            },
            row_data: {
                type: Object,
                default: () => {
                    return {}
                }
            },
            user_role: {
                type: String,
                default: () => {
                    return 'user'
                }
            },

        }
    }
</script>

<style scss>
    .v-table-row {
        display: flex;
        justify-content: space-around;
    }

    .row {
        flex-basis: 25%;
        padding: 8px 16px;
        text-align: left;
    }

    .row.row__name.bold {
        font-weight: bold;
    }
</style>