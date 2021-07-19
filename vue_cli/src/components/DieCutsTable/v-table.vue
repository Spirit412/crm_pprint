<template>
    <div class="v-table">
        <div class="v-table__pagination">
            <div class="page"
                 v-for="character in characters"
                 :key="character"
                 :class="{'page__selected': character === sortChart }"
                 @click="characterClick(character)"
            >{{character}}
            </div>
        </div>
        <div class="v-table__header">
            <p @click="sortByNmae">#
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p>Z
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p>Высота штампа
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p>Эт по гор-ли
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p>Эт по верт-ли
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p>Отступ по гор-ли
                <i class="material-icons md-18">unfold_more</i>
            </p>
            <p>Отступ по верт-ли
                <i class="material-icons md-24">format_line_spacing</i>
            </p>
        </div>
        <div class="v-table__body">
            <v-table-row
                v-for="(row, index) in paginatedItems"
                :key="row.cut_name"
                :row_data="row"
                :user_role="userRole"
            />
        </div>
        <div class="v-table__pagination">
            <div class="page"
                 v-for="page in pages"
                 :key="page"
                 :class="{'page__selected': page === pageNumber }"
                 @click="pageClick(page)"
            >{{page}}
            </div>
        </div>
    </div>
</template>

<script>

    import vTableRow from "./v-table-row";
    import _ from "lodash";

    export default {
        name: "v-table",
        props: {
            diecuts_data: {
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
        data() {
            return {
                sortChart: 'A',
                itemsPerPage: 20,
                pageNumber: 1,
                characters: ["A", "D", "X", "Y", "PR"],
            }
        },
        components: {
            vTableRow
        },
        computed: {
            /**
             * Количество страниц пагинации
             */
            pages() {
                return Math.ceil(this.diecuts_data.length / this.itemsPerPage);
            },
            /**
             * Возвращает список штампов начинающихся на this.sortChart
             * @return {paginatedItems~} - возвращает список
             */
            paginatedItems() {
                let from = (this.pageNumber - 1) * this.itemsPerPage;
                let to = from + this.itemsPerPage;
                /**
                 * Фильтруем список штампов по первой букве имени штампа
                 */
                let resultSortChart = _.filter(this.diecuts_data, obj => new RegExp('^' + this.sortChart, 'i').test(obj.cut_name));
                return resultSortChart.slice(from, to);
            },
        },
        methods: {
            pageClick(page) {
                this.pageNumber = page;
            },
            /**
             * Метод слушающий characterClick и записывающий результат в sortChart
             * @param {character} - буква
             */
            characterClick(character) {
                this.sortChart = character
            },
            sortByNmae(){
                this.diecuts_data.sort((a,b) => a.cut_name.localeCompare(b.cut_name))
            }
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
        flex-basis: 15%;
        text-align: left;
        cursor: pointer;
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