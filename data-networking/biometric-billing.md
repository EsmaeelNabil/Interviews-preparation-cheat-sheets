[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 34. Biometric Authentication & In-App Billing

### Biometric Authentication

> **TL;DR:** Use `BiometricPrompt.authenticate()` to show fingerprint/face auth dialog. Override `AuthenticationCallback` for success/error. Combine with `CryptoObject` for secure operations.

BiometricPrompt · Fingerprint/Face · CryptoObject · Callback-based

<details>
<summary>💻 Code Example</summary>

```kotlin
val biometricPrompt = BiometricPrompt(this, ContextCompat.getMainExecutor(this),
    object : BiometricPrompt.AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) {
            val cipher = result.cryptoObject?.cipher
            decryptUserToken(cipher)
        }
        override fun onAuthenticationError(errorCode: Int, errString: CharSequence) {
            showError("Auth failed: $errString")
        }
    }
)

val promptInfo = BiometricPrompt.PromptInfo.Builder()
    .setTitle("Authenticate").setSubtitle("Verify identity").setNegativeButtonText("Cancel").build()
biometricPrompt.authenticate(promptInfo)
```

</details>

### Google Play Billing

> **TL;DR:** Initialize `BillingClient` → `queryProductDetailsAsync()` to list products → `launchBillingFlow()` to start purchase. Handle `BillingResult` for success/error.

BillingClient · queryProductDetails · launchBillingFlow · Purchase state tracking

<details>
<summary>💻 Code Example</summary>

```kotlin
val billingClient = BillingClient.newBuilder(context).setListener { billingResult, purchases ->
    if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
        purchases?.forEach { processPurchase(it) }
    }
}.build()

billingClient.queryProductDetailsAsync(QueryProductDetailsParams.newBuilder()
    .setProductIds(listOf("premium")).setProductType(BillingClient.ProductType.SUBS).build()
) { _, products -> showProducts(products) }

val params = BillingFlowParams.newBuilder().setProductDetailsParamsList(list).build()
billingClient.launchBillingFlow(activity, params)
```

</details>

---

