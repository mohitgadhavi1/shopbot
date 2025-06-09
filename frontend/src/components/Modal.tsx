import { useState } from "react";
import { X, User, UserPlus } from "lucide-react";
import { LoginForm } from "./LoginForm";
import { SignupForm } from "./SignupForm";

interface AuthModalProps {
  isOpen: boolean;
  onClose: () => void;
  onAuthChange: (isLoggedIn: boolean) => void;
}

export default function AuthModal({
  isOpen,
  onClose,
  onAuthChange,
}: AuthModalProps) {
  const [activeTab, setActiveTab] = useState<"login" | "signup">("login");

  const handleSuccess = (access: string) => {
    const isLoggedIn = access !== null;
    onAuthChange(isLoggedIn);
    if (isLoggedIn) {
      onClose();
    } else {
      // Handle login failure if needed
      console.error("Login failed");
    }
  };

  const handleBackdropClick = (e: React.MouseEvent) => {
    if (e.target === e.currentTarget) {
      // onClose();
    }
  };

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 backdrop-blur-sm bg-opacity-50 flex items-center justify-center p-4 z-50 animate-in fade-in duration-200"
      onClick={handleBackdropClick}
    >
      <div className="bg-white rounded-xl shadow-2xl w-full max-w-md transform transition-all duration-200 animate-in zoom-in-95">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-100">
          <h2 className="text-xl font-semibold text-gray-800">
            {activeTab === "login" ? "Welcome Back" : "Create Account"}
          </h2>
          <button
            disabled
            onClick={onClose}
            className="p-2 hover:bg-gray-100 rounded-full transition-colors cursor-pointer"
            aria-label="Close modal"
          >
            <X size={20} className="text-gray-500" />
          </button>
        </div>

        {/* Tab Navigation */}
        <div className="flex bg-gray-50 mx-6 mt-6 rounded-lg p-1">
          <button
            className={`flex-1 flex cursor-pointer items-center justify-center gap-2 px-4 py-2 rounded-md font-medium transition-all duration-200 ${
              activeTab === "login"
                ? "bg-white text-blue-600 shadow-sm"
                : "text-gray-600 hover:text-gray-800"
            }`}
            onClick={() => setActiveTab("login")}
          >
            <User size={16} />
            Sign In
          </button>
          <button
            className={`flex-1 flex items-center cursor-pointer justify-center gap-2 px-4 py-2 rounded-md font-medium transition-all duration-200 ${
              activeTab === "signup"
                ? "bg-white text-green-600 shadow-sm"
                : "text-gray-600 hover:text-gray-800"
            }`}
            onClick={() => setActiveTab("signup")}
          >
            <UserPlus size={16} />
            Sign Up
          </button>
        </div>

        {/* Form Content */}
        <div className="p-6">
          <div className="mb-4">
            <p className="text-sm text-gray-600">
              {activeTab === "login"
                ? "Sign in to your account to continue"
                : "Join us today and get started"}
            </p>
          </div>

          {activeTab === "login" ? (
            <LoginForm onLoginSuccess={handleSuccess} />
          ) : (
            <SignupForm onLoginSuccess={handleSuccess} />
          )}

          {/* Additional Options */}
          <div className="mt-6 text-center">
            <p className="text-sm text-gray-600">
              {activeTab === "login"
                ? "Don't have an account? "
                : "Already have an account? "}
              <button
                onClick={() =>
                  setActiveTab(activeTab === "login" ? "signup" : "login")
                }
                className="text-blue-600 hover:text-blue-700 font-medium transition-colors cursor-pointer"
              >
                {activeTab === "login" ? "Sign up here" : "Sign in here"}
              </button>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
