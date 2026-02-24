[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 30. SSL/TLS & Network Security

### Certificate Pinning

> [!WARNING]
> **Pin specific certificates (SHA256 hash) to prevent MITM attacks.** Add pins to OkHttpClient. Generate pin:
> `openssl s_client | openssl x509 | openssl dgst`.

CertificatePinner · SHA256 pins · Backup pins · OkHttp integration

<details>
<summary>💻 Code Example</summary>

```kotlin
val pinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAAAAA==")  // Primary
    .add("api.example.com", "sha256/BBBBBBB==")  // Backup
    .build()

val httpClient = OkHttpClient.Builder()
    .certificatePinner(pinner)
    .build()

val retrofit = Retrofit.Builder().client(httpClient).build()
```

</details>

**Why:** Normal TLS validates cert against system store. Pinning = only trusts specific pins (harder to MITM even if store compromised).

<details>
<summary>🔩 Under the Hood</summary>

### Certificate Chain Validation

**TLS normally:** Client receives cert chain → validates against system CA store → trusts if any CA matches.

**With pinning:** Client verifies cert chain, then checks if public key hash matches pinned hash. Extra verification layer.

**Pin types:**
- Certificate pin (cert hash)
- Public key pin (public key hash, survives cert renewal)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Pin certificates for extra security" | Pinning = public key hash verification. Even if CA compromised, attacker needs matching public key. |
| "Pin primary + backup" | Primary pin rotates annually. Backup pins allow rotation without app update. Pin set can include 2-3 keys. |
| "Breaks app if pin expires" | If all pins expire/invalid, SSL handshake fails = app can't connect. Requires app update to fix (emergency). |

### Gotchas at depth

- **Pin expiry:** If you forget to rotate pins before cert expires, ALL users locked out. Must plan ahead.
- **Backup pins essential:** Never pin only one cert. Always include backup (prevents lockout).
- **Dynamic pin updates:** Enterprise apps can use dynamic pin updates (server tells client new pins). Complex but safer.

</details>

### Network Security Configuration

> [!TIP]
> Define per-domain security policies in `network_security_config.xml`. Set certificate trust anchors, disable
> cleartext. Reference in AndroidManifest.

Per-domain policies · Trust anchors · Cleartext control · Dev server exceptions

<details>
<summary>💻 Code Example</summary>

```xml
<!-- res/xml/network_security_config.xml -->
<network-security-config>
    <domain-config cleartextTrafficPermitted="false">
        <domain includeSubdomains="true">api.example.com</domain>
        <trust-anchors>
            <certificates src="@raw/my_ca" />
        </trust-anchors>
    </domain-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">10.0.0.1</domain>  <!-- Dev only -->
    </domain-config>
</network-security-config>

<!-- AndroidManifest.xml -->
<application android:networkSecurityConfig="@xml/network_security_config">
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### System Trust

**By default:** Android uses system's default CA list (Mozilla root certs bundled in OS).

**With custom trust anchors:** Framework validates cert against specified CAs only (ignores system store for that domain).

**Per-domain:** Can have different rules per server. Dev server allows HTTP, production enforces HTTPS.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Set trust anchors per domain" | NetworkSecurityConfig generates X509TrustManager per domain. OkHttp queries it during SSL handshake. |
| "cleartextTrafficPermitted controls HTTP" | Post-Android 9, HTTP disabled by default. cleartextTrafficPermitted="true" allows. Dev use only. |
| "Dev exceptions prevent app breakage" | Developers need localhost/10.0.0.0 for testing. Config allows selective exceptions without compromising prod. |

### Gotchas at depth

- **Certificate mismatch:** Custom CA must issue cert for domain name. Mismatch = SSL error despite CA in trust list.
- **Cleartext upgrade attacks:** Allowing HTTP = vulnerable to downgrade attacks. Only for dev/testing, never production.
- **Config inheritance:** Default-config applies globally unless domain-config overrides. Order matters.

</details>

---

