import joblib
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QuestionnaireResponse
from .serializers import QuestionnaireResponseSerializer

class QuestionnaireResponseView(APIView):

    # Define the recommendations logic outside of the post method
    def get_recommendations(self, status):
        if status == 1:
            return "Consider relaxation techniques like breathing exercises."
        else:
            return "Maintain a healthy routine and consider mindfulness practices."

    def post(self, request):
        # Deserialize the incoming data
        serializer = QuestionnaireResponseSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the data if valid
            serializer.save()
            
            # Load the trained ML model
            model = joblib.load('mental_health_model.pkl')
            
            # Get the input data from the serializer
            data = serializer.data
            # Predict the mental health status using the model
            prediction = model.predict([[data['phq9_score'], data['gad7_score']]])

            # Get the recommendations based on the prediction
            recommendation = self.get_recommendations(prediction[0])

            # Return the prediction and recommendation in the response
            return Response({
                'prediction': prediction[0],
                'recommendation': recommendation
            }, status=201)
        
        return Response(serializer.errors, status=400)
