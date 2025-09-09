import axios from "axios";
import { useState } from "react";

export default function useQuestionAnswer() {
    const [answer, setAnswer] = useState("");
    const [loading, setloading] = useState(false);
    const [error, setError] = useState(null);

    async function fetchAnswer(query) {
        if (!query) {
            setloading(false);
            setError("Query cannot be empty");
            return;
        }
        try {
            const response = await axios.get("/answer", {
                params: { query },
            });
            setAnswer(response.data.answer);
        } catch (err) {
            setError(err.message || "An error occurred while fetching the answer");
        } finally {
            setloading(false);
        }
    }

    return {answer, loading, error, fetchAnswer}
    
}