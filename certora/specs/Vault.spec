using ERC20Mock as asset;

methods {
    function totalSupply() external returns uint256 envfree;
    function redeem(uint256, address, address) external returns (uint256);
    function mint(uint256, address) external returns (uint256);
}

/**
* Property 1: Property "Mint by user must increase totalSupply".
* Rule that proves minting increases totalSupply of shares of the vault
*/
rule mintIncreasesTotalShareSupply(uint256 shares, address receiver) {
    env e;
    mathint total_supply_before = totalSupply();

    // call the mint function in the contract
    mint(e, shares, receiver);

    // totalSupply of shares after minting
    mathint total_supply_after = totalSupply();

    // minting increases the totalSupply of shares in the system
    assert total_supply_after == total_supply_before + shares, "total supply should increase after minting";
}

/**
* Property 2: Property "Redeem by user must decrease totalSupply".
* Rule that proves that redemption decrease totalSupply of shares of the vault
*/
rule redeemDecreasesTotalShareSupply(uint256 shares, address receiver, address owner) {
    env e;
    require receiver != currentContract && owner != currentContract;
    
    mathint total_supply_before_redemption = totalSupply();
    // filters out unreachable states with shares greater than the totalSupply
    require total_supply_before_redemption >= to_mathint(shares);

    redeem(e, shares, receiver, owner);

    mathint total_supply_after_redemption = totalSupply();

    // assert that the totalSupply of shares should be decreased by redeemed amount of shares
    assert total_supply_after_redemption == total_supply_before_redemption - shares, "total supply of shares should be decreased by amount of redeemed shares";
}
