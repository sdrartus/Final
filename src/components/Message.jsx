import React, { useContext, useEffect, useRef } from "react";
import { AuthContext } from "../context/AuthContext";
import { ChatContext } from "../context/ChatContext";

function whitespace(word) {
  if (word === "shit") {
    word = "crap";
  }
  return word;
}

//TEXT PREPROCESSING 
const Message = ({ message }) => {
  const { currentUser } = useContext(AuthContext);
  const { data } = useContext(ChatContext);

  const ref = useRef();

  useEffect(() => {
    ref.current?.scrollIntoView({ behavior: "smooth" });
  }, [message]);

  return (
    <div
      ref={ref}
      className={`message ${message.senderId === currentUser.uid && "owner"}`}
    >
      <div className="messageInfo">
        <img
          src={
            message.senderId === currentUser.uid
              ? currentUser.photoURL
              : data.user.photoURL
          }
          alt=""
        />
        <span>just now</span> {/* can change this */}
      </div>
      <div className="messageContent">
        <p>{message.text} </p> {/* filter */}
        {message.img && <img src={message.img} alt="" />}
      </div>
    </div>
  );
};

export default Message;
