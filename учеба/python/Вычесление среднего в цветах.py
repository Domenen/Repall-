flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}
# ===============================================================================
iris_set = flowers["iris_setosa"]["sepal_length"]
iris_vin = flowers["iris_virginica"]["sepal_length"]
iris_ver = flowers["iris_versicolor"]["sepal_length"]
slen = 0

mean_sepal_length_max = []
for iris in iris_set:
    mean_sepal_length_max.append(iris)
for iris in iris_vin:
    mean_sepal_length_max.append(iris)
for iris in iris_ver:
    mean_sepal_length_max.append(iris)
for iris in mean_sepal_length_max:
    slen = slen + iris
    mean_sepal_length = slen / len(mean_sepal_length_max)
print(mean_sepal_length)
# ===========================================================================
iris_set = flowers["iris_setosa"]["sepal_width"]
iris_vin = flowers["iris_virginica"]["sepal_width"]
iris_ver = flowers["iris_versicolor"]["sepal_width"]
slen = 0

mean_sepal_width_max = []
for iris in iris_set:
    mean_sepal_width_max.append(iris)
for iris in iris_vin:
    mean_sepal_width_max.append(iris)
for iris in iris_ver:
    mean_sepal_width_max.append(iris)
for iris in mean_sepal_width_max:
    slen = slen + iris
    mean_sepal_width = slen / len(mean_sepal_width_max)
print(mean_sepal_width)
# ===========================================================================
iris_set = flowers["iris_setosa"]["petal_length"]
iris_vin = flowers["iris_virginica"]["petal_length"]
iris_ver = flowers["iris_versicolor"]["petal_length"]
slen = 0

mean_petal_length_max = []
for iris in iris_set:
    mean_petal_length_max.append(iris)
for iris in iris_vin:
    mean_petal_length_max.append(iris)
for iris in iris_ver:
    mean_petal_length_max.append(iris)
for iris in mean_petal_length_max:
    slen = slen + iris
    mean_petal_length = slen / len(mean_petal_length_max)
print(mean_petal_length)