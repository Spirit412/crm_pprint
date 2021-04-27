<template>
    <div class="v-table-row">
        <div class="row row__cut_name bold">{{row_data.cut_name}}</div>
        <div class="row row__zub_num">{{row_data.zub_num}}</div>
        <div class="row row__vsheet">{{row_data.vsheet}}</div>
        <div class="row row__hcountitem">{{row_data.hcountitem}}</div>
        <div class="row row__vcountitem">{{row_data.vcountitem}}</div>
        <div class="row row__hgap">{{row_data.hgap}}</div>
        <div class="row row__vgap">{{row_data.vgap}}</div>
        <div class="row row__tbl_edit" v-if="user_role === 'admin'">
            <button class="btn-small btn">
                <i class="material-icons">open_in_new</i>
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "v-table-row",
        props: {
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
        flex-basis: 15%;
        padding: 8px 16px;
        text-align: left;
    }

    .row.row__cut_name.bold {
        font-weight: bold;
    }
</style>