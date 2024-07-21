const style_ok_response = () => {
    document.querySelector("#layout_main_panel_bottom").style.backgroundColor = '#deffbd';
    setTimeout(function () {
        document.querySelector("#layout_main_panel_bottom").style.backgroundColor = '#fcfcfc';
    }, 1000);
}

const style_error_response = () => {
    document.querySelector("#layout_main_panel_bottom").style.backgroundColor = '#ffc4c4';
    setTimeout(function () {
        document.querySelector("#layout_main_panel_bottom").style.backgroundColor = '#fcfcfc';
    }, 1000);
}

export const get_all_unit = () => {
    fetch('/units')
        .then(response => response.json())
        .then(data => {
            var tabledata = data;

        })
        .catch((error) => {
            document.querySelector("#layout_main_panel_bottom").innerHTML = "Error:" + error
            style_error_response()
        });
}

