<template>
    <div class="v-table">
        <div class="v-table__header">
            <p class="index">#
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p class="name">Заказчик
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p class="descript">Описание
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p v-if="userRole === 'admin'">EDIT
                <i class="material-icons md-24">mode_edit</i>
            </p>
        </div>
        <div class="v-table__body">
            <v-table-row
                v-for="(row, index) in data"
                :key="row.digitaljob_num"
                :row_data="row"
                :user_role="userRole"
            />
        </div>
    </div>
</template>

<script>

    import vTableRow from "./v-table-row";
    import _ from "lodash";

    export default {
        name: "v-djobs-table",
        props: {
            data: {
                type: Array,
                default: () => {
                    return []
                },
            },

            userRole: {
                type: String,
                default: () => {
                    return 'user'
                },
            }

        },
        components: {
            vTableRow
        },
    }

</script>

<style>
    .material-icons.md-18 {
        font-size: 18px;
        padding-left: 15px;
    }
    .material-icons.md-24 {
        font-size: 24px;
        padding-left: 15px;
    }
    .material-icons.md-32 {
        font-size: 32px;
        padding-left: 15px;
    }

    .v-table {
        max-width: 95%;
        margin: 0 auto;
    }

    .v-table__header {
        display: flex;
        justify-content: space-around;
        border-bottom: solid 1px #e7e7e7;
        font-size: 8pt;
    }

    .v-table__header p {
        display: flex;
        align-items: center;
        flex-basis: 5%;
        text-align: left;
        cursor: pointer;
    }

    .v-table__header p.name{
        display: flex;
        align-items: center;
        flex-basis: 20%;
        text-align: left;
        cursor: pointer;
        /*background: cornflowerblue;*/
    }

    .v-table__header p.descript{
        display: flex;
        align-items: center;
        flex-basis: 60%;
        text-align: left;
        cursor: pointer;
        /*background: #42b983;*/
    }

    .v-table__header p.index{
        display: flex;
        align-items: center;
        flex-basis: 5%;
        text-align: left;
        cursor: pointer;
        /*background: #8b42b9;*/
    }

    .v-table__pagination {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 30px;
    }

    .page {
        padding: 8px;
        margin-right: 10px;
        border: solid 1px #e7e7e7;
    }

    .page:hover {
        background: #aeaeae;
        cursor: pointer;
        color: white;
    }

    .page__selected {
        background: #aeaeae;
        cursor: pointer;
        color: white;
    }
</style>