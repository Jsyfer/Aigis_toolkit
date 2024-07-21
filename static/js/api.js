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

export const update_by_id = (cell) => {
    fetch('/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            update_key: cell.getRow().getIndex(),
            update_field: cell.getField(),
            update_value: cell.getRow().getData()[cell.getField()]
        })
    })
        .then(response => response.json())
        .then(data => {
            let data_log = ""
            data.result.forEach(item => {
                data_log = data_log + item + "<br/>"
            })
            document.querySelector("#layout_main_panel_bottom").innerHTML = data_log
            style_ok_response()
        })
        .catch((error) => {
            document.querySelector("#layout_main_panel_bottom").innerHTML = "Error:" + error
            style_error_response()
        });
}

