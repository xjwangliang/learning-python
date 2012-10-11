package com.taobao.api.response;

import com.taobao.api.internal.mapping.ApiField;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.simba.login.authsign.get response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class SimbaLoginAuthsignGetResponse extends TaobaoResponse {

	private static final long serialVersionUID = 2439557957319679324L;

	/** 
	 * 登陆签名
	 */
	@ApiField("subway_token")
	private String subwayToken;

	public void setSubwayToken(String subwayToken) {
		this.subwayToken = subwayToken;
	}
	public String getSubwayToken( ) {
		return this.subwayToken;
	}

}
