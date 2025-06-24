from flask import Flask, render_template, request, redirect, url_for
from forms import ProductForm
from models import Product
from ext import app, db

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ProductForm()

    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            image=form.image.data
        )

        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for("index"))

    products = Product.query.all()
    return render_template("index.html", form=form, products=products)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)

    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.image = form.image.data
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("edit.html", form=form, product=product)

@app.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete_product(id):
    product = Product.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("confirm_delete.html", product=product)


if __name__ == "__main__":
    app.run(debug=True)
