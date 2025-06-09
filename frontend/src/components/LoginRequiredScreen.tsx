import { Lock, MessageCircle } from "lucide-react";

// LoginRequiredScreen Component
const LoginRequiredScreen = ({
  onLoginClick,
}: {
  onLoginClick: () => void;
}) => (
  <div className="flex-1 flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 h-screen">
    <div className="text-center max-w-md mx-auto p-8">
      <div className="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-6">
        <Lock className="w-10 h-10 text-blue-600" />
      </div>

      <h2 className="text-2xl font-bold text-gray-900 mb-4">Login Required</h2>

      <p className="text-gray-600 mb-8 leading-relaxed">
        Please log in to access ShopBot and start chatting with our AI
        assistant. Get personalized product recommendations and shopping help!
      </p>

      <div className="space-y-4">
        <button
          onClick={onLoginClick}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl font-medium transition-colors flex items-center justify-center space-x-2"
        >
          <MessageCircle className="w-5 h-5" />
          <span>Login to Start Shopping</span>
        </button>

        <div className="flex items-center justify-center space-x-6 text-sm text-gray-500">
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-green-500 rounded-full"></div>
            <span>AI Assistant</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
            <span>Product Search</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
            <span>Smart Recommendations</span>
          </div>
        </div>
      </div>
    </div>
  </div>
);

export default LoginRequiredScreen;
