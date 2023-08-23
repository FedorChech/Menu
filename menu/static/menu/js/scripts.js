

document.addEventListener("DOMContentLoaded", function() {
    const formContainer = document.querySelector(".form");
    const addFormButton = document.getElementById("add-form");
    const formsetPrefix = "{{ dish_product_formset.prefix }}";

    addFormButton.addEventListener("click", function() {
        const totalFormsInput = document.getElementById(`id_${formsetPrefix}-TOTAL_FORMS`);
        const formCount = parseInt(totalFormsInput.value);
        const newForm = document.createElement("div");
        newForm.innerHTML = `
            <div class="form-group">
                <label for="id_${formsetPrefix}-${formCount}-product">Продукт</label>
                <select name="${formsetPrefix}-${formCount}-product" id="id_${formsetPrefix}-${formCount}-product">
                    ${productOptions}
                </select>
                <label for="id_${formsetPrefix}-${formCount}-grams">Граммы</label>
                <input type="number" name="${formsetPrefix}-${formCount}-grams" id="id_${formsetPrefix}-${formCount}-grams">
            </div>
        `;
        formContainer.appendChild(newForm);

        totalFormsInput.value = formCount + 1;
    });
});

