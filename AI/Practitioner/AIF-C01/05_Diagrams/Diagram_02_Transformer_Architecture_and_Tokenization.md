# Diagram 02: Transformer Architecture and Tokenization

> **Architecture Blueprint:** `Diagram_02_Transformer_Architecture_and_Tokenization.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Domain Alignment:** Domain 2 (Generative AI Fundamentals)

---

## 🏛️ Architectural Blueprint

```mermaid
flowchart TD
    subgraph Tokenization["1. Tokenization & Vector Space"]
        RawText["Raw Text:\n'AWS Bedrock accelerates generative AI'"] --> Tokenizer["Tokenizer (e.g., BPE)"]
        Tokenizer --> Tokens["Token IDs: [1542, 8934, 12044, 451, 982]"]
        Tokens --> EmbedLayer["Token Embeddings + Positional Encodings\n(Dense D-dimensional Vectors)"]
    end

    subgraph TransformerCore["2. Transformer Decoder Layer (Repeated N Times)"]
        EmbedLayer --> MaskedAttn["Masked Multi-Head Self-Attention\nAttention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V"]
        MaskedAttn --> AddNorm1["Residual Add & Layer Normalization"]
        AddNorm1 --> FFN["Feed-Forward Neural Network (MLP)"]
        FFN --> AddNorm2["Residual Add & Layer Normalization"]
    end

    subgraph OutputGen["3. Probability Distribution & Token Selection"]
        AddNorm2 --> LinearHead["Linear Classification Head"]
        LinearHead --> Logits["Raw Logits over Vocabulary"]
        Logits --> Softmax["Softmax Layer with Temperature T\nP(w_i) = exp(z_i / T) / sum(exp(z_j / T))"]
        Softmax --> Sampling["Sampling Strategy\n(Top-P Nucleus / Top-K / Greedy)"]
        Sampling --> NextToken["Next Generated Token:\n'applications'"]
    end
```

---

## 🔍 Core Architectural Highlights

1. **Self-Attention Mechanics:** Allows each token to attend to every other token simultaneously using learned Query ($Q$), Key ($K$), and Value ($V$) projections.
2. **Causal Masking:** Ensures decoder-only foundation models (like Amazon Nova or Claude) can only look at past tokens, preventing future token leakage during text generation.
3. **Sampling Control:** 
   * Temperature T → 0 collapses the distribution into deterministic greedy argmax.
   * Higher $T$ flattens the distribution, increasing linguistic diversity.
   * Top-P restricts generation to the dynamic set of top tokens whose cumulative probability exceeds $P$.
