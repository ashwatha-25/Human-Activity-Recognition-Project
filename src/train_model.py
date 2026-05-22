if accuracy > best_accuracy:

    best_accuracy = accuracy
    best_model = model
    joblib.dump(
    best_model,
    "../models/best_model.pkl"
)