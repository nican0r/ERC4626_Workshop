# ERC4626 Workshop Inflation Attack
Repository adapted from the Certora workshop on ERC4626 at TrustX @ Istanbul 2023.

The certora folder contains Certora CVL specification for the [inflation attack](https://tienshaoku.medium.com/eip-4626-inflation-sandwich-attack-deep-dive-and-how-to-solve-it-9e3e320cc3f1) on ERC4626 where the attack implemented in the specification aims to cover a more generalized version of the attack to make it more broadly applicable. 

The verification is checked against OpenZeppelin's [implementation of ERC4626](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/extensions/ERC4626.sol).

# Getting started

1. [Sign-up for Certora Free Tier](https://www.certora.com/signup?plan=prover)
* _Note: It's important to also set the CERTORAKEY environment variable._
2. Install the [Certora prover](https://docs.certora.com/en/latest/docs/user-guide/getting-started/install.html#)
3. Run the Vault specification by executing `certoraRun certora/conf/Vault.conf` from within the ERC4626_Workshop folder to view the initial rules verified for the vault. Follow the link returned and wait for the verification to be completed. Alternatively, open the [pre-computed results](https://prover.certora.com/output/51488/0544a074c96b498a893b3f5fa67e9a0d/?anonymousKey=e987db8e13f3635bc61bb95196a75d5291d2ebd7).
4. Run the InflationAttack specification by executing `certoraRun certora/conf/InflationAttack.conf` from within the ERC4626_Workshop folder. Follow the link returned and wait for the verification to be completed. Alternatively, open the [pre-computed results](https://prover.certora.com/output/51488/d09e191668d54fcba2e6ffb3da6a4185/?anonymousKey=57153d4eb0dcb8fd11d603a57ffeac86a3ef2c3a).
 
# Additional Material

* [Prover Documentation](https://docs.certora.com/en/latest/)
* [ERC-4626 Specifications](https://ethereum.org/en/developers/docs/standards/tokens/erc-4626/)
* [Inflation Attack](https://tienshaoku.medium.com/eip-4626-inflation-sandwich-attack-deep-dive-and-how-to-solve-it-9e3e320cc3f1)
