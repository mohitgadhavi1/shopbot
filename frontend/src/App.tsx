import { useState, useRef, useEffect } from "react";
import {
  Send,
  Search,
  ShoppingCart,
  Star,
  Heart,
  Filter,
  X,
} from "lucide-react";

import AuthModal from "./components/Modal.tsx";

interface Product {
  id: number;
  name: string;
  price: number;
  originalPrice: number;
  image: string;
  rating: number;
  reviews: number;
  category: string;
  description: string;
}

interface Message {
  id: number;
  type: "bot" | "user";
  content: string;
  timestamp: Date;
  products?: Product[];
}

interface CartItem extends Product {
  quantity: number;
}

const EcommerceChatbot = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      type: "bot",
      content:
        "Welcome to ShopBot! I can help you find products, answer questions, and assist with your shopping. What are you looking for today?",
      timestamp: new Date(),
    },
  ]);
  const [inputValue, setInputValue] = useState<string>("");
  const [isTyping, setIsTyping] = useState<boolean>(false);
  const [showProductModal, setShowProductModal] = useState<boolean>(false);
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);
  const [cartItems, setCartItems] = useState<CartItem[]>([]);
  const [cartCount, setCartCount] = useState<number>(0);
  const [products, setProducts] = useState<Product[]>([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    console.log(!!localStorage.getItem("access"));
    setIsLoggedIn(!!localStorage.getItem("access"));
  }, []);

  const [showModal, setShowModal] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const handleLogout = () => {
    localStorage.clear();
    setIsLoggedIn(false);
    setShowModal(true);
  };

  // Mock product data
  useEffect(() => {
    const accessToken = localStorage.getItem("access");
    console.log(accessToken);
    {
      const accessToken = localStorage.getItem("access");
      if (isLoggedIn && accessToken) {
        fetch("https://shopbot-jla9.onrender.com/api/products/", {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        })
          .then((res) => res.json())
          .then((data: Product[]) => setProducts(data))
          .catch((err) => console.error("Error:", err));
      }
    }
  }, [isLoggedIn]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const addToCart = (product: Product, quantity: number = 1) => {
    const existingItem = cartItems.find((item) => item.id === product.id);
    if (existingItem) {
      setCartItems(
        cartItems.map((item) =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + quantity }
            : item
        )
      );
    } else {
      setCartItems([...cartItems, { ...product, quantity }]);
    }
    setCartCount((prevCartCount) => prevCartCount + quantity);

    // Add confirmation message
    const botMessage: Message = {
      id: Date.now(),
      type: "bot",
      content: `Great! I've added ${product.name} to your cart. You now have ${
        cartCount + quantity
      } item(s) in your cart.`,
      timestamp: new Date(),
    };
    setMessages((prev) => [...prev, botMessage]);
  };

  const handleSendMessage = () => {
    if (!inputValue.trim()) return;

    const userMessage: Message = {
      id: Date.now(),
      type: "user",
      content: inputValue,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInputValue("");
    setIsTyping(true);

    // Simulate bot response
    setTimeout(() => {
      const botResponse: Message = generateBotResponse(inputValue);
      setMessages((prev) => [...prev, botResponse]);
      setIsTyping(false);
    }, 1000);
  };

  const generateBotResponse = (userInput: string): Message => {
    const input = userInput.toLowerCase();
    let response = "";
    let products_to_show: Product[] = [];

    if (
      input.includes("headphone") ||
      input.includes("audio") ||
      input.includes("music")
    ) {
      response =
        "I found some great headphones for you! Here are our top recommendations:";
      products_to_show = products.filter(
        (p) => p.category === "Electronics" && p.name.includes("Headphones")
      );
    } else if (
      input.includes("watch") ||
      input.includes("fitness") ||
      input.includes("health")
    ) {
      response = "Perfect! Here are some excellent fitness watches:";
      products_to_show = products.filter((p) => p.name.includes("Watch"));
    } else if (
      input.includes("shirt") ||
      input.includes("clothing") ||
      input.includes("wear")
    ) {
      response = "Here are some popular clothing items:";
      products_to_show = products.filter((p) => p.category === "Clothing");
    } else if (
      input.includes("gaming") ||
      input.includes("keyboard") ||
      input.includes("computer")
    ) {
      response = "Great choice! Here are some gaming accessories:";
      products_to_show = products.filter((p) => p.name.includes("Gaming"));
    } else if (input.includes("cart") || input.includes("checkout")) {
      response = `You have ${cartCount} item(s) in your cart. Would you like to proceed to checkout?`;
    } else if (
      input.includes("price") ||
      input.includes("cheap") ||
      input.includes("budget")
    ) {
      response = "Here are some budget-friendly options:";
      products_to_show = products.filter((p) => p.price < 50);
    } else {
      response = "Here are some popular products you might like:";
      products_to_show = products.slice(0, 2);
    }

    return {
      id: Date.now(),
      type: "bot",
      content: response,
      products: products_to_show,
      timestamp: new Date(),
    };
  };

  const ProductCard = ({
    product,
    isInModal = false,
  }: {
    product: Product;
    isInModal?: boolean;
  }) => (
    <div
      className={`bg-white rounded-xl shadow-lg overflow-hidden ${
        isInModal ? "max-w-md mx-auto" : "w-full max-w-sm"
      } transition-transform hover:scale-105`}
    >
      <div className="relative">
        <img
          src={product.image}
          alt={product.name}
          className="w-full h-48 object-cover"
        />
        <button className="absolute top-3 right-3 p-2 bg-white rounded-full shadow-lg hover:bg-gray-50">
          <Heart className="w-4 h-4 text-gray-600" />
        </button>
      </div>

      <div className="p-4">
        <h3 className="font-semibold text-gray-900 mb-2 line-clamp-2">
          {product.name}
        </h3>

        <div className="flex items-center mb-2">
          <div className="flex items-center">
            {[...Array(5)].map((_, i) => (
              <Star
                key={i}
                className={`w-4 h-4 ${
                  i < Math.floor(product.rating)
                    ? "text-yellow-400 fill-current"
                    : "text-gray-300"
                }`}
              />
            ))}
            <span className="ml-1 text-sm text-gray-600">
              ({product.reviews})
            </span>
          </div>
        </div>

        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center space-x-2">
            <span className="text-xl font-bold text-gray-900">
              ${product.price}
            </span>
            <span className="text-sm text-gray-500 line-through">
              ${product.originalPrice}
            </span>
          </div>
          <span className="text-xs bg-red-100 text-red-800 px-2 py-1 rounded-full">
            Save ${(product.originalPrice - product.price).toFixed(2)}
          </span>
        </div>

        {isInModal && (
          <p className="text-gray-600 mb-4 text-sm">{product.description}</p>
        )}

        <div className="flex space-x-2">
          <button
            onClick={() => addToCart(product)}
            className="flex-1 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-medium transition-colors flex items-center justify-center space-x-2"
          >
            <ShoppingCart className="w-4 h-4" />
            <span>Add to Cart</span>
          </button>
          <button
            onClick={() => {
              setSelectedProduct(product);
              setShowProductModal(true);
            }}
            className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
          >
            View
          </button>
        </div>
      </div>
    </div>
  );

  return (
    <>
      <div className="flex flex-col h-screen bg-gray-50 w-screen ">
        {/* Header */}
        <div className="bg-white border-b border-gray-200 px-4 py-3 flex items-center justify-between ">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 bg-amber-200-600 rounded-lg flex items-center justify-center">
              <img src="/vite.svg" alt="Vite Logo" className="w-4 h-4" />
            </div>
            <div>
              <h1 className="font-semibold text-gray-900 line-clamp-4">
                ShopBot
              </h1>
              <p className="text-xs text-gray-500">Online • Ready to help</p>
            </div>
          </div>

          <div className="flex items-center space-x-3">
            {isLoggedIn ? (
              <button
                onClick={handleLogout}
                className="bg-red-500 text-white px-4 py-2 rounded cursor-pointer"
              >
                Logout
              </button>
            ) : null}
            <button className="relative p-2 text-gray-500 hover:bg-gray-100 cursor-pointer rounded-lg ">
              <ShoppingCart className="w-5 h-5" />
              {cartCount > 0 && (
                <span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
                  {cartCount}
                </span>
              )}
            </button>
            <button className="p-2 text-gray-500 hover:bg-gray-100 cursor-pointer  rounded-lg">
              <Filter className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`flex ${
                message.type === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`max-w-xs sm:max-w-md lg:max-w-lg xl:max-w-xl ${
                  message.type === "user"
                    ? "bg-blue-600 text-white rounded-l-2xl rounded-tr-2xl rounded-br-sm"
                    : "bg-white text-gray-900 rounded-r-2xl rounded-tl-2xl rounded-bl-sm shadow-sm border border-gray-100"
                } px-4 py-3`}
              >
                <p className="text-sm">{message.content}</p>

                {message.products && message.products.length > 0 && (
                  <div className="mt-4 space-y-3">
                    <div className="grid gap-3 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-1 xl:grid-cols-2">
                      {message.products.map((product) => (
                        <ProductCard key={product.id} product={product} />
                      ))}
                    </div>
                  </div>
                )}

                <p className="text-xs opacity-70 mt-2">
                  {message.timestamp.toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit",
                  })}
                </p>
              </div>
            </div>
          ))}

          {isTyping && (
            <div className="flex justify-start">
              <div className="bg-white rounded-r-2xl rounded-tl-2xl rounded-bl-sm shadow-sm border border-gray-100 px-4 py-3">
                <div className="flex space-x-1">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                  <div
                    className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                    style={{ animationDelay: "0.1s" }}
                  ></div>
                  <div
                    className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                    style={{ animationDelay: "0.2s" }}
                  ></div>
                </div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Input */}
        <div className="bg-white border-t border-gray-200 p-4">
          <div className="flex items-center space-x-3">
            <div className="flex-1 relative">
              <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
                placeholder="Ask about products, prices, or anything else..."
                className="w-full px-4 py-3 pr-12 bg-gray-100  rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-colors"
              />
              <button className="absolute right-3 top-1/2 transform -translate-y-1/2 ">
                <Search className="w-4 h-4 text-gray-500 hover:bg-gray-100   " />
              </button>
            </div>
            <button
              onClick={handleSendMessage}
              disabled={!inputValue.trim()}
              className="p-3 bg-blue-600 hover:bg-blue-700   disabled:bg-gray-300 disabled:text-gray-500 text-gray-100 cursor-pointer  rounded-2xl transition-colors"
            >
              <Send className="w-4 h-4" />
            </button>
          </div>

          <div className="flex flex-wrap gap-2 mt-3">
            {[
              "Show headphones",
              "Fitness watches",
              "Gaming gear",
              "Budget items",
            ].map((suggestion) => (
              <button
                key={suggestion}
                onClick={() => setInputValue(suggestion)}
                className="px-3 py-1 text-xs bg-gray-100 hover:bg-gray-200 text-gray-500 rounded-full cursor-pointer transition-colors"
              >
                {suggestion}
              </button>
            ))}
          </div>
        </div>

        {/* Product Modal */}
        {showProductModal && selectedProduct && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-2xl max-w-md w-full max-h-[90vh] overflow-y-auto">
              <div className="p-6">
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-xl font-bold">Product Details</h2>
                  <button
                    onClick={() => setShowProductModal(false)}
                    className="p-2 hover:bg-gray-100 rounded-lg"
                  >
                    <X className="w-5 h-5" />
                  </button>
                </div>

                <ProductCard product={selectedProduct} isInModal={true} />

                <div className="mt-6 flex space-x-3">
                  <button
                    onClick={() => {
                      addToCart(selectedProduct);
                      setShowProductModal(false);
                    }}
                    className="flex-1 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl font-medium transition-colors"
                  >
                    Add to Cart
                  </button>
                  <button className="flex-1 bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-xl font-medium transition-colors">
                    Buy Now
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {isLoggedIn ? null : (
        <AuthModal
          isOpen={showModal}
          onClose={() => {
            setIsLoggedIn(!!localStorage.getItem("access"));
            setShowModal(false);
          }}
          onAuthChange={(e) => console.log(e)}
        />
      )}
    </>
  );
};

export default EcommerceChatbot;
