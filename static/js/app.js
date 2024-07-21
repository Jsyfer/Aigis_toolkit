import * as api from "./api.js";

window.onload = function () {
    table.setData("/units");
};

//create Tabulator on DOM element with id "example-table"
var table = new Tabulator("#example-table", {
    height: "100%",// set height of table (in CSS or here), this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
    layout: "fitColumns", //fit columns to width of table (optional)
    placeholder: "No Data Set",
    columns: [ //Define Table Columns
        { title: "ID", field: "id", width: 50, headerFilter: "number" },
        {
            title: "画像", field: "icon", width: 70, formatter: "image", hozAlign: "center", formatterParams: {
                height: "50px",
                width: "50px",
            }
        },
        { title: "名前", field: "unit_name", editor: "input", headerFilter: "input" },
        {
            title: "リア",
            field: "rare",
            width: 70,
            editor: "list",
            editorParams: { autocomplete: "true", listOnEmpty: true, valuesLookup: true },
            headerFilter: true, headerFilter: "list",
            headerFilterParams: { valuesLookup: true, clearable: true }
        },
        { title: "所持済", field: "owned", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
        { title: "覚醒済", field: "is_awakening", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
        { title: "交流クエスト", field: "has_extra_story", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
        { title: "交流クエストクリア", field: "complete_extra_story", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
        { title: "育成済", field: "all_complete", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
    ],
});